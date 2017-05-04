factories.
	factory('UserHttp', ['$http', function($http){
		products = {}
		products.login = function(username, password){
			data = {
				username : username,
				password : password
			}
			return $http.post("/rest-auth/login/", data)
		}
		
		return products
	}])