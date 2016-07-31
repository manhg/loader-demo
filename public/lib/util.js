define(function(require) {
  var _ = require('vendor/lodash')
  return {
    great: function() {
      console.log(_.capitalize('lodash works!'))
    }
  }
})
