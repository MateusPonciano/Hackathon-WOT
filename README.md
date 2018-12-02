# Hackathon-WOT
O projeto consiste em quatro componentes explicados abaixo:

  blink.py: programa que na raspberry pi que capta sensor de movimento e envia comandos de apagar e acender para os leds

  admin-painel: painel de controle aberto no browser no qual são mostrados quais leds estão acesos e quais estão apagados
  
  central.py: programa onde são precessadas as regras para apagar ou acender os leds
  
  flow.json: flow do node-red que utiliza um server http para receber os comandos e envia para o painel via websockets
  
