<template>
  <nav>
      <v-row>
          <v-col
          cols=4
          >
            <img src="..\assets\lombard-logo.png" alt="">
          </v-col>
          <v-col
          cols=4
          class="nav-list"
          >
            <router-link to="/">
                <div class="nav-tab">addItem</div>
            </router-link>
            <router-link to="/add">
                <div class="nav-tab">listItem</div>
            </router-link>
            <router-link to="/summary">
                <div class="nav-tab">summary</div>
            </router-link>
          </v-col>
      </v-row>
  </nav>
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
.nav-tab{
    display: inline;
}
</style>
