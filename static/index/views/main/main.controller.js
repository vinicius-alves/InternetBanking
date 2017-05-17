'use strict';

angular.module('app')
.controller('Main.Controller', Controller);




function Controller($scope, $http, prefix, $location, AuthenticationService){

	$scope.loading = false;

	var updateBalance = function(){

		$scope.loading = true;

		$http.post(prefix + '/balance/')
        .then(function (response) {

            $scope.balance = response.data.balance;
            $scope.loading = false;
            
        }, function(response){
            
           $scope.balance_message = response.data.error;
           $scope.loading = false;           
        });
	};

	updateBalance();

	$scope.withdraw = function(){

		$scope.loading = true;

		$http.post(prefix + '/withdraw/',{ value : $scope.withdraw_value })
        .then(function (response) {

            updateBalance();
            if($scope.asked_excerpt) $scope.excerpt();
            $scope.withdraw_message = "Sacado!";
            $scope.loading = false;
            $scope.withdraw_value = null;
            
        }, function (response){
            
           $scope.withdraw_message = response.data.error;
           $scope.loading = false;
        });
	};

	$scope.deposit = function(){

		$scope.loading = true;

		$http.post(prefix + '/deposit/',{ value : $scope.deposit_value })
        .then(function (response) {

            updateBalance();
            if($scope.asked_excerpt) $scope.excerpt();            
            $scope.deposit_message = "Depositado!";
            $scope.loading = false;
            $scope.deposit_value = null;
            
        }, function (response){
            
           $scope.deposit_message = response.data.error;
           $scope.loading = false;
        });
	};

	$scope.transfer = function(){

		$scope.loading = true;

		$http.post(prefix + '/transfer/',{ value : $scope.transfer_value, receiver : parseInt($scope.transfer_receiver)})
        .then(function (response) {

            updateBalance();
            if($scope.asked_excerpt) $scope.excerpt();
            $scope.transfer_message = "Transferido!";
            $scope.loading = false;
            $scope.transfer_value = null;
            
        }, function (response){
            
           $scope.transfer_message = response.data.error;
           $scope.loading = false;
        });
	};

	$scope.excerpt = function(){

		$scope.asked_excerpt = true;

		$scope.loading = true;

		$http.post(prefix + '/excerpt/')
        .then(function (response) {

            $scope.excerpt_message = "";
            $scope.loading = false;
            $scope.excerpt_transactions = response.data.transactions;
            $scope.excerpt_button="hidden";
            
        }, function (response){
            
           $scope.excerpt_message = response.data.error;
           $scope.loading = false;
        });
	};

	$scope.help = function(){


		$scope.loading = true;

		$http.post(prefix + '/help/')
        .then(function (response) {

          $scope.help_button="hidden";
        	updateBalance();
            if($scope.asked_excerpt) $scope.excerpt();
            $scope.help_message = "Requerimento enviado!";
            $scope.loading = false;
            
        }, function (response){
            $scope.help_button="hidden";
            $scope.help_message = response.data.detail;
            $scope.loading = false;
        });
	};

	$scope.logout = function(){

		AuthenticationService.logout();
		$location.path('/login');

	};

};