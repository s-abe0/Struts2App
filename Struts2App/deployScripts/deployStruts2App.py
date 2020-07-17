deployEAR="/opt/IBM/WebSphere/AppServer/earFiles/Struts2App.ear"
appManager="AdminControl.queryNames('cell=nullNode01Cell,node=wasNode01,type=ApplicationManager,process=server1,*')

# Install the app
def installStruts2App:
    AdminApp.install(deployEAR, "[-appname Struts2AppEAR]")
    AdminConfig.save()
    
    AdminControl.invoke(appManager, 'startApplication','Struts2AppEAR')

# Update the app
def updateStruts2App:
    AdminApp.update('Struts2AppEAR', 'app', '[-operation update -contents /opt/IBM/WebSphere/AppServer/earFiles/Struts2App.ear -usedefaultbindings -nodeployejb]')
    AdminConfig.save()i

installStruts2App()
updateStruts2App()