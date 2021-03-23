FROM redmine:4.1.2-passenger

# Install patch
RUN apt-get update && apt-get -y upgrade && apt-get -y install patch

# Copy in patch file and logo
COPY --chown=redmine:redmine misc/base.html.erb.patch /usr/src/redmine/app/views/layouts/base.html.erb.patch
COPY --chown=redmine:redmine misc/logo.png /usr/src/redmine/public/images/logo.png

# Apply patch to base html template for logo
RUN patch /usr/src/redmine/app/views/layouts/base.html.erb < /usr/src/redmine/app/views/layouts/base.html.erb.patch

# Copy in patch for formatter
COPY misc/formatter.rb.patch /usr/src/redmine/lib/redmine/wiki_formatting/markdown/formatter.rb.patch

# apply patch to Markdown formatter
RUN patch /usr/src/redmine/lib/redmine/wiki_formatting/markdown/formatter.rb < /usr/src/redmine/lib/redmine/wiki_formatting/markdown/formatter.rb.patch

# Setup home directory as landing spot for native passenger library
RUN mkdir -p /home/redmine && chown redmine.redmine /home/redmine
