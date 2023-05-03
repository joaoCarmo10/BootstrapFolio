import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import time


app = Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ, "/Assets/style.css"])
server = app.server


#cards about

formacao1 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("MBA em Engenharia de Negócios e Gestão de Empresas", className="card-title", style={'text-align':'center'}),
            html.P("Baiana Business school (2022 - Atual)", className="card-title", style={'text-align':'center'}),
            html.P("MBA em Gestão")
        ], style={'text-align':'center', 'display':'flex', 'flex-direction':'column', 'justify-content':'center', "width":"25rem"}
    )
)
formacao2 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Graduação em Engenharia de produção", className="card-title", style={'text-align':'center'}),
            html.P("Centro Universitário Senai Cimatec (2016 - 2021)", className="card-title", style={'text-align':'center'}),
            html.P("Graduação em Engenharia")
        ], style={'text-align':'center', 'display':'flex', 'flex-direction':'column', 'justify-content':'center', "width":"25rem"}
    )
)
formacao3 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Ensino Médio", className="card-title", style={'text-align':'center'}),
            html.P("Colégio Salesiano do Salvador (2002 - 2012)", className="card-title", style={'text-align':'center'}),
            html.P("Ensino Médio Regular")
        ], style={'text-align':'center', 'display':'flex', 'flex-direction':'column', 'justify-content':'center', "width":"25rem"}
    )
)

formacao = dbc.Row(
    [
        dbc.Col(formacao1, className="mb-4 h-100 col-md-4 mx-auto col-10", width={'size': 12, 'order': 1, 'offset': '0'}),
        dbc.Col(formacao2, className="mb-4 h-100 col-md-4 mx-auto col-10", width={'size': 12, 'order': 2, 'offset': '0'}),
        dbc.Col(formacao3, className="mb-4 h-100 col-md-4 mx-auto col-10", width={'size': 12, 'order': 3,'offset': '0'}),
    ],
    className=
    #"mt-4"
    "container-fluid",
    style={"display": "flex", "flex-wrap": "wrap", "justify-content": "center"},
)

#Navbar
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

#Footer
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

#Pagina Home
grid1 = html.Div([
    dbc.Row([
        dbc.Col([
            html.Div([
                html.P([html.H5("Bem-vindo(a), ", className='h5', style={"width":"80%", "text-align": "center"})]),
                html.P("Meu nome é João Pedro do Carmo Costa Santos, sou Engenheiro de Produção, atualmente trabalhando como Analista de Custos e como Consultor de Business Intelligence.", className='hp', style={"width":"80%", "text-align": "Justify"}),
                dbc.Row([
                    dbc.Col([
                        dbc.Button("Projetos", className="btn", style={"width":"100%"})
                    ], md=5, lg =5, sm=12),
                    dbc.Col([
                        dbc.Button("Sobre mim", className="btn", style={"width":"100%"})
                    ], md=5, lg =5, sm=12),
                    dbc.Col([
                        html.Img(src='/Assets/pdf.png', style={"width":"100%"})
                    ], md=2, lg=2, sm=12),
                ])       
            ])
        ],md = 5, lg = 5, sm = 12)
    ], style={"margin-left":"10%"})
])

# Pagina About
grid2 = html.Div([
    dbc.Row(
        dbc.Col(
            html.Img(
                src="https://media.licdn.com/dms/image/D4D03AQFP4olXaQdzGw/profile-displayphoto-shrink_800_800/0/1680175468993?e=1688601600&v=beta&t=oTIYwvFWVdYI1jS0TF41wwWJ1QKjduBVvgn6g3CA1L8",
                height=100,
                style={"display": "block", "margin": "auto", "border-radius":"50px"}
            ),
            width=12
        )
    ),
    dbc.Row(
        dbc.Col(
            html.P(
                "Me chamo João Pedro do Carmo Costa, sou formado em Engenharia de Produção no Centro Universitário Senai Cimatec, possuo Certificado Six Sigma Green Belt, atualmente estou cursando MBA em Engenharia de Negócios e Gestão de Empresas na Baiana Business School e sou apaixonado pela área de DADOS. Ah, também sou um triatleta!"
            ),
            width=12,
            style={"margin-top":"10px"}
        )
    ),
   dbc.Row(
    [
        dbc.Col(
            dbc.Button("Formação", style={"width":"100%", "margin-bottom":"10px"}, className="text-center"),md=3, lg=3, sm=12,
            className="d-flex justify-content-center mb-2 mb-sm-0"
        ),
        dbc.Col(
            dbc.Button("Experiência", style={"width":"100%", "margin-bottom":"10px"},className="text-center"),md=3, lg=3, sm=12,
            className="d-flex justify-content-center mb-2 mb-sm-0"
        ),
        dbc.Col(
            dbc.Button("Stack", style={"width":"100%", "margin-bottom":"10px"},className="text-center"),md=3, lg=3, sm=12,
            className="d-flex justify-content-center mb-2 mb-sm-0"
        ),
        dbc.Col(
            dbc.Button("Serviços", style={"width":"100%", "margin-bottom":"10px"},className="text-center"),md=3, lg=3, sm=12,
            className="d-flex justify-content-center"
        ),
    ],
    justify="center",
    style={"margin-top":"20px"},
    className="flex-wrap flex-column flex-sm-row"
),
    dbc.Row([
            dbc.Col(formacao1, className="mb-4 h-100 d-flex", md=3, lg=4, sm=12),
            dbc.Col(formacao2, className="mb-4 h-100 d-flex",  md=3, lg=4, sm=12),
            dbc.Col(formacao3, className="mb-4 h-100 d-flex",  md=3, lg=4, sm=12),
    ],
    className="flex-wrap flex-column flex-sm-row",
    style={"justify-content": "center", "flex-wrap": "wrap"}
    ),
])

card = html.Div([
    dbc.Col(
        dbc.Card(
            (dbc.CardBody([html.Div(grid1, style={'text-align': 'center'}),], id='card1')),
            className='mycard-container'
        ), md=8, lg=8, sm=12, style={'text-align': 'center'}
    )
])

sessao1 = html.Div(
    [
        dbc.Container(grid1, className="my-4"),
    ]
)

app.layout = html.Div(
    [
        navbar,       
        sessao1,
        grid2,   
        footer                      
    ], 
)


if __name__ == "__main__":
    app.run_server(port=8000, debug=True)