import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
#import sass


app = Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])
server = app.server

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home")),
        dbc.NavItem(dbc.NavLink("Sobre")),
        dbc.NavItem(dbc.NavLink("Portfólio")),
        dbc.NavItem(dbc.NavLink("Contato")) 
    ],
    brand="João Pedro",
    #brand_href="#",
    className="navbar-transparent",
    color="#000000",
    #color='white',
    dark=True,
    sticky='top',
    #style={'borderBottom': 'none', 'height': '60px', 'transparent':'true'
           #'backgroundColor': 'black', 'opacity':'0.5'
    #}, 
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


grid1 = html.Div(
    dbc.Row([
        dbc.Col([
            html.A(html.Img(src = "https://media.licdn.com/dms/image/D4D03AQFP4olXaQdzGw/profile-displayphoto-shrink_800_800/0/1680175468993?e=1687996800&v=beta&t=xDFEeXdRTFn5plY_xP9ZTv-Xs703V9CBfAHsJSOFjlo", height="100px",style={"margin-left": "10px", "border-radius": "50%", 'align':'center'})),
            html.P(html.H5( "Bem-vindo(a), ",style={"text-align": "center", "margin-top":"50px"})),
            html.P("Meu nome é João Pedro do Carmo Costa Santos, sou Engenheiro de Produção, atualmente trabalhando como Analista de Custos e como Consultor Autônomo de Business Intelligence.")]
        ,width={
                'size': 12, 
                'order': 1, 
                #'offset': 2,
                }, md=12
            ),
        #dbc.Col(
           # html.A(html.Img(src = "https://media.licdn.com/dms/image/D4D03AQFP4olXaQdzGw/profile-displayphoto-shrink_800_800/0/1680175468993?e=1687996800&v=beta&t=xDFEeXdRTFn5plY_xP9ZTv-Xs703V9CBfAHsJSOFjlo", height="200px",style={"margin-left": "10px", "border-radius": "50%"}))
            #,width={
             #   'size':12,
              #  'order':2,
               # 'offset':1
            #}, md=4
        #)
    ]), style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center', 'height': '50vh', 'text-align':'justify'}
    
)

card = dbc.Card(
    dbc.CardBody(
        grid1
    ),style={"background-image": "linear-gradient(to bottom right, #007bff, #000000)"}
    
)


content = dbc.Container(
    dbc.Row(
        dbc.Col(
            card,
            width={"size": 6, 
                   "offset": 3,
                   "align":"center"
                   },
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
        "background-image": "linear-gradient(to bottom right, #007bff, #000000)",
    }
)

app.layout = html.Div([navbar, 
                       content,
                       footer
                       ], style={"background-image": "linear-gradient(to bottom right, #007bff, #000000)"})

if __name__ == "__main__":
    app.run_server(port=8000, debug=True)