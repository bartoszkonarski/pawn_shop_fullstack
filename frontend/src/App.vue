<template>
  <section id="app">
    <navBar 
    :logged="logged"
    @logOut="changeLogState"
    > </navBar>
    <router-view
    :logged="logged"
    ></router-view>
  </section>
</template>

<script>
import navBar from './components/navBar.vue';
export default {
  name: 'App',
  components: {
    navBar: navBar,
  },
  data: function() {
    return{
      logged: true,
    }
  },
  methods:{
    changeLogState: function(){
      this.logged = false;
    }
  }
}
</script>

<style>
body {
  margin: 0px;
  background: #663EFF;
}
</style>
