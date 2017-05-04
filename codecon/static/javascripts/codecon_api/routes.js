var module = angular.module('Routes', ['ui.router'])

module.config(['$stateProvider', '$urlRouterProvider', 
	function($stateProvider, $urlRouterProvider) {
	$urlRouterProvider.otherwise("/home")
	
	$stateProvider
		.state('index', {
			url : '/home',
			templateUrl : '/static/pages/index.html'
		})
		.state('register', {
			url : '/register',
			templateUrl : '/static/pages/register.html',
			controller : 'UserController'
		})

}])