deployEAR="/opt/IBM/WebSphere/AppServer/earFiles/Struts2App.ear"

cell=AdminConfig.list('Cell')
cellname=AdminConfig.showAttribute(cell, 'name')
nodename=AdminConfig.showAttribute(AdminConfig.list('Node', cell), 'name')

appManager=AdminControl.queryNames('cell=' + cellname + ',node=' + nodename + ',type=ApplicationManager,process=server1,*')

# Install the app
def installStruts2App:
    AdminApp.install(deployEAR, "[-appname Struts2AppEAR]")
    AdminConfig.save()
    
    AdminControl.invoke(appManager, 'startApplication','Struts2AppEAR')

# Update the app
def updateStruts2App:
    AdminApp.update('Struts2AppEAR', 'app', '[-operation update -contents /opt/IBM/WebSphere/AppServer/earFiles/Struts2App.ear -usedefaultbindings -nodeployejb]')
    AdminConfig.save()

installStruts2App()
updateStruts2App()