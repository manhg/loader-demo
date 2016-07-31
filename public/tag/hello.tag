<x-hello>
  <h1>Welcome</h1>
  <span>{ today }</span>
  <div>{ hash }</div>
  <script>
  var self = this
  this.today = new Date();

  curl(['vendor/md5'], function(md5) {
    self.update({
      'hash': md5(':)')
    })
  })
  </script>
</x-hello>
