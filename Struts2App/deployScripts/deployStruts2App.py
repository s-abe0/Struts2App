deployEAR="/opt/IBM/WebSphere/AppServer/earFiles/Struts2App.ear"

# Install the app
#AdminApp.install(deployEAR, "[-appname Struts2AppEAR]")
#AdminConfig.save()

# Update the app
AdminApp.update('Struts2AppEAR', 'app', '[-operation update -contents /opt/IBM/WebSphere/AppServer/earFiles/Struts2App.ear -usedefaultbindings -nodeployejb]')
AdminConfig.save()
