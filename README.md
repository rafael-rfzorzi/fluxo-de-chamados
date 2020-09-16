# fluxo-de-chamados

Story:

Pensando em uma situação em que a empresa X atenda milhares de clientes pelo país,
através de suas regionais, por meio de chamados realizados pelos seus clientes através de aplicativos, preenchendo alguns dados vitais ao atendimento do mesmo, para que estas informações cheguem até a filial responsável pelo suporte a região do cliente, onde este chamado irá passar por processo de fila de atendimento, seguindo alguns critérios.

Da parte do cliente, ele ira gerar o chamado e aguardar pelo atendimento.

Detalhamento do fluxo:

Precisamos primeiro definir os atores deste atendimento, de um lado temos o cliente com sua solicitação, de outro temos o(s) técnico(s) que irá realizar o serviço solicitado.
No meio disto temos o fluxo de controle desta logística de atendimento.

Definindo os objetos deste fluxo:

1 – Cliente: 
	O cliente possui um problema com seu equipamento, ele acessa o aplicativo e informa dados relativos a sua matricula, região, localização, tipo de serviço, criticidade, problema ocorrido, data de realização do chamado  etc..

2 – Central de atendimento:
	A central de atendimento recebe  as solicitações, separa cada chamado por região e distribui os mesmos de acordo com a Central regional que ira realizar este atendimento. 
	
3 – Centrais Regionais:
	Cada Central regional recebe seus respectivos chamados, separando primeiramente por tipo de atendimento, cada tipo de atendimento irá para uma fila de acordo com o tipo de profissional que ira realizar o atendimento(Eletricista, Mecânico etc..)
	Dentro da fila do Profissional X, teremos um número X de profissionais aptos a atender os chamados, destes alguns estarão em atendimento, outros estarão aguardando um chamado.
	Nesse momento temos 2 filas dentro de uma especialidade de atendimento, a dos chamados e dos técnicos.
	Com estas informações em mãos, se faz necessário realizar um cruzamento destas informações, utilizando condicionais de acordo com certos critérios de prioridade, tais como criticidade de atendimento, disponibilidade do técnico, distância do técnico em relação ao atendimento etc..
	Do cruzamento destes dados temos enfim uma fila onde o chamado tem seus dados construídos, com status do chamado, técnico(s) etc... 
