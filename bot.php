<?php
##request del webhook
$website = "https://api.telegram.org/bot%BOTTOKEN%";

#lee y decodificar lo que dice el webhook
$update = json_decode(file_get_contents('php://input'), TRUE);

#extraer información entrante del webhook
$chatId = $update['message']['chat']['id']; #que id tiene el mensaje
#$chatType = $update["message"]["chat"]["type"]; #que tipo de chat es
$message = $update['message']['text']; #mensaje entrante

#Obtener el día.
setlocale(LC_TIME,"es_CO");
$dia = strftime("%A");
function fecha(){
    GLOBAL $dia;
    return $dia;
}

#Guardar horario del usuario u obtener si existe [work in progress]
function horario(){
    GLOBAL $chatId;
    $response = "works.".$chatId;
    return $response;
}

#Comandos y respuestas [not complete]
switch ($message) {
    case '/horario': #muestra el horario [work in progress]
        $response = " horario";
        sendMessage($chatId, $response);
        break;
        
    case '/hoy': #muestra las materias de "hoy" [work in progress]
        $response = "Hoy ".utf8_encode($dia)." te toca: ";
        sendMessage($chatId, $response);  
        break;
        
    case '/addhorario': #Comando que añade y guarda el horario [work in progress]
        sendMessage($chatId,horario());
        break;
}

#Funcion para enviar el mensaje.
function sendMessage($chatId, $response){
    $url = $GLOBALS['website'].'/sendMessage?chat_id='.$chatId.'&parse_mode=HTML&text='.urlencode($response);
    file_get_contents($url);
}
?>