controllers.
	controller('RegisterController', ['$location', '$http','$scope', 'AccountFactory', 
		function($location, $http, $scope, AccountFactory){
			var ctrl = this
			$scope.register = function(){
				console.log($scope.first_name)
				console.log($scope.last_name)
				console.log($scope.email)
				console.log($scope.username)
				console.log($scope.password)
				console.log($scope.conf_password)
			}
			AccountFactory.post(
				'Arjemariel', 'Requina', 
				'killbill@gmail.com', 'killbill', 
				'killbill')
					.then(function(response){
						console.log(response.data)
				     })
			// $http({
			// 	url : '/api/accounts/',
			// 	method : 'GET'
			// }).then(function(response){
			// 	console.log(response)
			// })
		}])
