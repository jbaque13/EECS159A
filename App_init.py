from guizero import App

def app_init():
	app = App(title="Mira", layout="grid",height=1024,width=600) #originally bg=black. deleted it so it could go back to the original "None" -Jorge
	#app.full_screen = True
	return app
