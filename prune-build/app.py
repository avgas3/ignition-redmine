
from redminelib import Redmine
import datetime
import os, sys, argparse, yaml, time, logging, requests
# Setup Logger
logger = logging.getLogger('tina_project_copy')
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s:%(name)s:%(levelname)s: %(message)s'))
logger.addHandler(console_handler)
logger.debug("starting")
# Constants
CONNECTION_ERROR_REST_TIME_SECONDS = 15

def main(poll_frequency):
    # Start Main Loop
    while 1:
        next_poll_time = time.time() + float(poll_frequency)
        connection_error = False
        logger.debug("checking...")
        try:
            # Setup Redmine Connection
            redmine = Redmine(redmine_server_url, key=redmine_api_key)
            
            #Check each project to see if it has pruning enabled. 
            projects = redmine.project.all()
            prune_projects = []
            logger.debug("found " + str(len(projects)) + " projects")
            for project in projects:
                enable = project['custom_fields'].get(2).value
                if project['custom_fields'].get(2).value == '1': # custom_field id 2 is Prune Enable
                    logger.debug("Project found with pruning enabled.")
                    maxage = project['custom_fields'].get(3).value  #pull the max age, id==3
                    cutoff = datetime.datetime.now() - datetime.timedelta(days=int(maxage))
                    prune_issues = redmine.issue.filter(project=project['identifier'])
                    for issue in prune_issues:
                        if issue['updated_on'] < cutoff:
                            logger.info(project['name']+ ": Rejecting issue #" + str(issue['id'])+" - " + issue['subject'])
                            logger.info("Last updated on " + str(issue['updated_on']))
                            redmine.issue.update(issue['id'],status_id=6) # Rejected

        except requests.exceptions.ConnectionError as e:
            logger.error(e)
        finally:
            # Rest for configured time seconds
            
            time.sleep(max(0.0, next_poll_time - time.time()))



if __name__ == "__main__":


    # Load from config and secrets yamls
    #config = yaml.safe_load(open(args.config))
    #secrets = yaml.safe_load(open(args.secrets))
    redmine_api_key = '41d9f7a01a7633f4cca275e053d4c85d4ebf5a2f'#secrets['redmine_api_key']
    redmine_server_url = 'http://redmine:3000/redmine'#config['redmine_server_url']
    sys.exit(main(poll_frequency=5))