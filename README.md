# PhychoBlog

## heroku
```
heroku git:remote psychoblog
heroku pg:backups:capture --app psychoblog

heroku pg:backups:schedule DATABASE_URL --at '02:00 America/Los_Angeles' --app psychoblog

```