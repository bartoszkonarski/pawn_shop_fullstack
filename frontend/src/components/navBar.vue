<template>
  <section 
  class="nav-container"
  >
    <div class="nav-logo">
      <img src="../../src/assets/lombard-logo.png" alt="">
    </div>
    
    <div class="nav-link-container">

      <router-link to="/">
        <div class="nav-tab" style="background-color: #96F04D">
          addItem
        </div>
      </router-link>

      <router-link to="/add">
        <div class="nav-tab" style="background-color: #50D98E">
          <font-awesome-icon icon="fa-solid fa-basket-shopping" />
        </div>
      </router-link> 

      <router-link to="/summary">
        <div class="nav-tab" style="background-color: #E6D149">
          summary
        </div>
      </router-link>  

    </div>
    <div style="clear:both"></div>

    

  </section>
</template>

<script>
import addItem from './content/addItem.vue';
import listItem from './content/listItem.vue';
export default {
  name: 'navBar',
  components: {
  },
  data: () => {
      return{
        addItem: addItem,
        listItem: listItem,
      }
  },
}
</script>

<style scoped>
.nav-container{
  background-color: #6666FF;
  height: 20vh;
}
.nav-link-container{
  float: left;
  width: 70vw;
  height: 14vh;
}
.nav-tab{
    display: block;
    background: red;
    width: 15%;
    height: 50%;
    margin: 3% 5%;
    float:inline-start;
    text-align: center;
    border-radius: 15px;
    box-shadow: -1px 15px 60px 0px rgba(0,0,0,0.75);
    -webkit-box-shadow: -1px 15px 60px 0px rgba(0,0,0,0.75);
    -moz-box-shadow: -1px 15px 60px 0px rgba(0,0,0,0.75);
}
.nav-logo{
  float: left;

}
img{
  width: 30vw;
  height: 14vh;
}
router-link{
 border-top: solid 4px white;
}
</style>
