import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import time


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

grid2 = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                html.P([html.H5("Bem-vindo(a), " ,className='h5')]),
                html.P("Meu nome é João Pedro do Carmo Costa Santos, sou Engenheiro de Produção, atualmente trabalhando como Analista de Custos e como Consultor Freelancer de Business Intelligence.", className='hp'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("Projetos", className="btn", style={"width":"100%"})
                    ], width=6),
                        dbc.Col([
                            dbc.Button("Sobre mim", className="btn", style={"width":"100%"})
                    ], width=6),
                    ])       
            ])
            ],width=6),
        dbc.Col([
            html.Div([
                html.A(html.Img(src="https://media.licdn.com/dms/image/D4D03AQFP4olXaQdzGw/profile-displayphoto-shrink_800_800/0/1680175468993?e=1687996800&v=beta&t=xDFEeXdRTFn5plY_xP9ZTv-Xs703V9CBfAHsJSOFjlo", 
                height="200px", style={"border-radius": "50%", "margin-left": "30px"})),
            ])
    ],width=6)
    ])
])


card = dbc.Container(
    dbc.Card(
        dbc.CardBody(grid2),
        className='card-container',
    )
)


app.layout = html.Div(
    [
        navbar,     
            html.Div(className='container-fluid',children=[       
                card
            ]),   
        footer                      
    ], 
)

if __name__ == "__main__":
    app.run_server(port=8000, debug=True)