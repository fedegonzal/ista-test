# exit on error
set -o errexit

cd railsapp
bundle install
bundle exec rails assets:precompile
bundle exec rails assets:clean
bundle exec rails db:migrate

#if you have seeds to run add:
# bundle exec rails db:seed
