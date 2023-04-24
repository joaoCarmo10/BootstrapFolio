import dash_bootstrap_components as dbc
from dash import Dash, html, dcc


app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server

# Menu lateral

#inserindo a navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home")),
        dbc.NavItem(dbc.NavLink("Sobre")),
        dbc.NavItem(dbc.NavLink("Portfólio")),
        dbc.NavItem(dbc.NavLink("Contato")) 
    ],
    brand="João Pedro",
    brand_href="#",
    color="#000000",
    #color='white',
    dark=True,
    sticky='top',
    style={'borderBottom': 'none', 'height': '60px'
           #'backgroundColor': 'black', 'opacity':'0.5'
    }, 
)

card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("JOÃO PEDRO DO CARMO", className="card-title")
            ,html.P("ENGENHEIRO DE PRODUÇÃO, ANALISTA DE CUSTOS, APAIXONADO POR DADOS E TRIATLETA.")        
        ]
    )
)

# Conteúdo principal
content = dbc.Container(
    dbc.Row(
        dbc.Col(
            card,
            width={"size": 10, "offset": 1},
            className="mt-5",
            style={
                "height": "65vh",
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
            }
        )
    ),
    fluid=True,
    style={
        "height": "92vh",
        #"background-image": "linear-gradient(to bottom right, #007bff, #000000)",
    }
)

footer = dbc.Container(    
    dbc.Row(
        dbc.Col(
            html.Div([
                html.P("Desenvolvido por João Pedro do Carmo, 2023 ", className="text-muted", style={"text-align": "center", "margin-top":"15px"}),
                html.A(html.Img(src=" https://cdn-icons-png.flaticon.com/512/3955/3955024.png ", height="30px", style={"margin-left": "10px"}), href="https://www.instagram.com/joaocarmo.co/", target="_blank"),
                html.A(html.Img(src="https://cdn-icons-png.flaticon.com/512/3955/3955051.png", height="30px",style={"margin-left": "10px"}), href="https://www.linkedin.com/in/joaodocarmo95/", target="_blank", className="ml-auto")
            ], 
                         
            className="d-flex align-items-center justify-content-center"),
            className="mt-2",
            style={"padding": "5px"}
        ),
    ),
    fluid=True,
    style={
         #"background-color": "#f8f9fa",
        #"border-top": "1px solid #000000",
        "position": "fixed",
        "bottom": "0",
        "width": "100%",            
    }
)


grid = html.H4( "Bem-vindo(a)",style={"text-align": "center", "margin-top":"50px"})
grid1 = html.Div(
    dbc.Row([
        dbc.Col(
            html.P("Meu nome é João Pedro do Carmo Costa Santos, sou Engenheiro de Produção, atualmente trabalhando como Analista de Custos e como Consultor Autônomo de Business Intelligence.")
        ,width={
                'size': 10, 
                'order': 1, 
                'offset': 1,
                }, md=4),
        dbc.Col(
            html.H1("Foto Profissional")
            ,width={
                'size':10,
                'order':2,
                'offset':1
            }, md=4
        )
    ]), style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center', 'height': '50vh', 'text-align':'justify'}
    
)

app.layout = html.Div([navbar, 
                       grid,
                       grid1,
                       footer
                       ])

if __name__ == "__main__":
    app.run_server(port=8000, debug=True)