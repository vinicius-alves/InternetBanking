"use strict";

angular
  .module('app')
  .service('AuthenticationService', Service);

/**
* @ngdoc service
* @name Mobits.service:AuthenticationService
* @description
* Responsável pelo processamento das requisições de login e logout.
*/    

function Service($http, $localStorage, prefix) {

    /**
    * @ngdoc method
    * @name login
    * @methodOf Joaninha.service:AuthenticationService
    * @description
    * Inicialmente processa os dados para login e depois os envia ao servidor para ober um Token, 
    * que é usado para fornecer acesso as demais requisições posteriores aos dados do usuário. <br/>
    * Recebe o email e senha, que devem ser previamente validados pela view.
    * Também recebe como argumento uma callback, que será executada quando finalizar a requisição.<br/>
    * Após este processamento inicial faz uma requisição com os dados processados para "/login/".<br/>
    * Caso não ocorra erro, salva o token no armazenamento local. <br/>
    * A partir daí toda nova requisição http possuíra estes campos.
    * @param {string} account O número da conta do usuário, disponível na view.
    * @param {string} password A senha do usuário, disponível na view.
    * @param {function} callback Callback a ser chamada após tentativa de realização do login
    */

    this.login = function(account, password, callback) {

        $http.post(prefix + '/login/', { username: account, password: password })
        .then(function loginSuccess(response) {

            $http.defaults.headers.common.Authorization = 'Token ' + response.data.token;
            $localStorage.currentUser={};
            $localStorage.currentUser.token=response.data.token;
            callback(true,response.data.message,response.status);
            
        }, function loginError(response){
            
            callback(false,response.data.non_field_errors[0],response.status);
        });
    };



    /**
    * @ngdoc method
    * @name logout
    * @methodOf Mobits.service:AuthenticationService
    * @description
    * Apaga todo o armazenamento local, incluindo o Token de acesso.<br/>
    * O que impossibilita de usuário ter acesso a dados da aplicação e a views restritas.
    */  

    this.logout = function() {
      $localStorage.$reset();
    }; 
};