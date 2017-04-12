var site_module = angular.module('Blog', ['Routes', 'Controllers'])
var controllers = angular.module('Controllers', ['Factories', 'Services'])
var services = angular.module('Services', [])
var factories = angular.module('Factories', [])
// var module = angular.module('Blog', ['Authentication', 
// 	'Registration', 'Routes', 'Config'])