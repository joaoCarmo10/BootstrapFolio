import dash_bootstrap_components as dbc
from dash import Dash, html, dcc


app = Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ, "/Assets/style.css"])
server = app.server

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home")),
        dbc.NavItem(dbc.NavLink("Sobre")),
        dbc.NavItem(dbc.NavLink("Portfólio")),
        dbc.NavItem(dbc.NavLink("Contato")) 
    ],
    brand="João Pedro",
    className="navbar-transparent",
    #color='#000000',
    dark=True,
    sticky='top',
    style={'borderBottom': 'none', 'height': '50px', 
           #'backgroundColor': '#000000'
           }, 
)

footer = dbc.Container(    
    dbc.Row(
        dbc.Col(
            html.Div([
                html.P("Desenvolvido por João Pedro do Carmo, 2023 ", className="text-muted", style={"text-align": "center", "margin-top":"15px"}),
                html.A(html.Img(src=" https://cdn-icons-png.flaticon.com/512/3955/3955024.png ", height="30px", style={"margin-left": "10px"}), href="https://www.instagram.com/joaocarmo.co/", target="_blank"),
                html.A(html.Img(src="https://cdn-icons-png.flaticon.com/512/3955/3955051.png", height="30px",style={"margin-left": "10px"}), href="https://www.linkedin.com/in/joaodocarmo95/", target="_blank", className="ml-auto")
            ], className="d-flex align-items-center justify-content-center"),
            className="mt-2",
            style={"padding": "5px"}
        ),
    ),
    fluid=True,
    style={
        "position": "fixed",
        "bottom": "0",
        "width": "100%",            
    }
)

grid1 = dbc.Container(
    dbc.Row([
        dbc.Col([
            html.P(html.H5("Bem-vindo(a), ", style={"text-align": "center", "margin-top": "50px"})),
            html.P("Meu nome é João Pedro do Carmo Costa Santos, sou Engenheiro de Produção, atualmente trabalhando como Analista de Custos e como Consultor Autônomo de Business Intelligence.")
        ]),
        dbc.Col([
            html.A(html.Img(src="https://media.licdn.com/dms/image/D4D03AQFP4olXaQdzGw/profile-displayphoto-shrink_800_800/0/1680175468993?e=1687996800&v=beta&t=xDFEeXdRTFn5plY_xP9ZTv-Xs703V9CBfAHsJSOFjlo", height="200px", style={"margin-left": "10px", "border-radius": "50%", "text-align": "center", "margin-top": "50px"}))
        ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'})
    ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center', 'height': '50vh', 'text-align': 'justify'}
))


card = dbc.Card(
    dbc.CardBody(grid1),
    className='card-container',
    #style={#"background-image": "linear-gradient(to bottom right, #007bff, #000000)", 
     #     'height':'80%', 'margin-left':'30px'}
)



content = dbc.Container(
    dbc.Row(
        dbc.Col(
            card,
            width={"size": 12, "md": 6},
            className="mt-5 d-flex align-items-center justify-content-center",
            style={"height": "65vh"}
        )
    ),
    fluid=True,
    style={
        "height": "93.5vh",
        #"background-image": "linear-gradient(to bottom right, #007bff, #000000)",
        "display": "flex"
    }
)

app.layout = html.Div([navbar,                        
                       content,                       
                       footer                       ], 
                       style={#"background-image": "linear-gradient(to bottom right, #007bff, #000000)",
                              "min-height": "100vh",
                              "background-size":"cover"})

if __name__ == "__main__":
    app.run_server(port=8000, debug=True)