"use strict";

var app = angular.module('app', ['ui.router', 'ngStorage','ngMessages']);

/**
* @ngdoc object
* @name Mobits.object:Router
* @description
*
*/

/**
* @ngdoc property
* @name Urls
* @propertyOf 
* @description
*
*/

app.constant("prefix", "/ws");

//public routes
app.config(function ($stateProvider) {
  $stateProvider
    .state('login', {
        url: '/login',
        templateUrl: 'views/login/login.view.html',
        controller: 'Login.Controller'
    });
});

//restricted routes
app.config(function ($stateProvider) {
  $stateProvider
    .state('main', {
        url: '/main',
        templateUrl: 'views/main/main.view.html',
        controller:'Main.Controller'
     });
});

app.config(function($urlRouterProvider){
    // default route
    $urlRouterProvider.otherwise("/main");
});


app.run(function($rootScope, $http, $location, $localStorage) {

    // set default header
    $http.defaults.headers.common.Accept = 'application/json';

    // keep user logged in after page refresh
    if ($localStorage.currentUser) {
      $http.defaults.headers.common.Authorization = 'Token ' + $localStorage.currentUser.token;
    }

    // redirect to login page if not logged in and trying to access a restricted page
    $rootScope.$on('$locationChangeStart', function (event, next, current) {
        var publicPages = ['/login'];
        var restrictedPage = publicPages.indexOf($location.path()) === -1;
        if (restrictedPage && !$localStorage.currentUser) {
            $location.path('/login');
        } 
    });
});