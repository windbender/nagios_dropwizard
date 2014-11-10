nagios_dropwizard
=================

This is a short python script which allows nagios to check the dropwizard (http://dropwizard.io)  "healthcheck" URL.

I'm no python guru, so once I got this working I stopped.  I'd be quite happy if someone with a few more python XP would submit a PR.

set this up via a command clause like this:

```
define command {
   command_name    check_http_dropwizard_healthcheck
   command_line    $USER1$/check_dropwizard.py $HOSTADDRESS$ $ARG1$ $ARG2$
}
```

And the the service definition would look like this:

```
define service{
        use             generic-service         ; Inherit default values from a template
        host_name       yourhosthere
        service_description  check for your dropwizard service
        check_command   check_http_dropwizard_healthcheck!8081!yourDWHealthcheck
}
```
