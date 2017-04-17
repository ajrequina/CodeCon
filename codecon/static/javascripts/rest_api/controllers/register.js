controllers.
	controller('RegisterController', ['$location', '$http','$scope', 'AccountFactory', 
		function($location, $http, $scope, AccountFactory){
			var ctrl = this
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
