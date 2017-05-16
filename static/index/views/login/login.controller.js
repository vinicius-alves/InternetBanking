'use strict';

angular.module('app')
.controller('Login.Controller', Controller);

/**
* @ngdoc controller
* @name Mobits.controller:Login
* @requires Mobits.service:AuthenticationService
* @description
* Controller da view "login". 
* Ao iniciar define a função de escopo de login.
* Também chama a função Logout do AuthenticationService, 
* garantindo que o usuário esteja deslogado.
*/


function Controller($scope,$location, AuthenticationService){

    $scope.loading = false;
    AuthenticationService.logout();

    /**
    * @ngdoc method
    * @name login
    * @methodOf Mobits.controller:Login
    * @description
    * Redireciona a requisição de login para o método 
    * {@link Mobits.service:AuthenticationService#methods_Login Login} do 
    * {@link Mobits.service:AuthenticationService AuthenticationService}.<br/>
    * Caso o resultado seja bem sucedido, redireciona o usuário para a view "main".<br/>
    * Caso não seja, exibe o erro ocorrido em um campo próprio na view.
    * @param {string} account O e-mail do usuário, disponível na view.
    * @param {string} password A senha do usuário, disponível na view de login.
    */
    
    $scope.login = function(){
        $scope.loading = true;
        AuthenticationService.login($scope.account, $scope.password, 
            function (success,message,status) {
                if (success) {
                    $location.path('/main');
                } else {
                    if(status<0){
                        $scope.error = 'Verifique sua conexão com a internet';
                    }else{
                        $scope.error = message;
                    }
                }
                $scope.loading = false;
        });
    };


};