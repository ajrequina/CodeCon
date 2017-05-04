controllers.
	controller('UserController', ['$location', '$http','$scope', 'UserHttp', 
		function($location, $http, $scope, UserHttp){
			var ctrl = this
			$scope.login = function(){
				UserHttp.login(
						$scope.username,
						$scope.password)
					.then(function(response){
						console.log(response)
					})
			}
			$scope.register = function(){
				AccountFactory.post(
					$scope.first_name, $scope.last_name, 
					$scope.email, $scope.username, 
					$scope.password, $scope.confirm_password )
						.then(function(response){
							console.log(response.data)
						})
			}
		}])