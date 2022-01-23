<template>
  <section>

      <div class="list-left-panel">
        <EditTiles 
        v-if="activeEdit"
        :name="activeItem.name" 
        :brand="activeItem.brand" 
        :state="activeItem.state" 
        :info="activeItem.info" 
        :cost="activeItem.cost" 
        :newCost="activeItem.newCost" 
        :id="activeItem.id"
        @editClick="editClick($event)"
        @cancelClick="cancelClick"
        />
      </div>

      <div class="list-right-panel">
        <Tiles 
        :name="item.name" 
        :brand="item.brand" 
        :state="item.state" 
        :info="item.info" 
        :cost="item.cost" 
        :newCost="item.newCost" 
        :id="item.id"
        v-for="item in items" 
        :key="item.id"
        @edit="editItem($event)"
        @del="deleteItem($event)"
        />
        <br>
      </div>

  </section>
</template>

<script>
import tiles from './listItem/tiles.vue'
import editTiles from './listItem/editTiles.vue' //VS Code ocipiał
import axios from 'axios';

export default {
  name: 'listItem',
  components: {
    Tiles: tiles,
    EditTiles: editTiles,
  },
  props: ['logged','tokken'],
  data: () => {
    return{
      items: [],
      activeItem: {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 0},
      activeEdit:false,
    }
  },
  methods: {
    editItem: function(itemToEdit) {
      this.activeItem.name = itemToEdit.name
      this.activeItem.cost = itemToEdit.cost
      this.activeItem.state = itemToEdit.state
      this.activeItem.info = itemToEdit.info
      this.activeItem.brand = itemToEdit.brand
      this.activeItem.newCost = itemToEdit.newCost
      this.activeItem.id = itemToEdit.id
      this.activeEdit = true;
      console.log(itemToEdit.name, itemToEdit.cost, itemToEdit.state, itemToEdit.info, itemToEdit.brand, itemToEdit.newCost, itemToEdit.id)
      console.log(this.activeItem.name, this.activeItem.cost, this.activeItem.state, this.activeItem.info, this.activeItem.brand, this.activeItem.newCost, this.activeItem.id)
    },
    deleteItem: function(id){
      // Funkcja która usuwa przedmioty.
      id
    },
    editClick: function(item){
      var result = confirm("Czy jesteś pewien że chcesz edytować ten obiekt?");
      if(result)
      {
          this.activeEdit = false;
        // axios.get(
        // 'http://127.0.0.1:5000/items',
        // { headers: {'Authorization': "Bearer "+this.$session.get('tokken')}}
        // )
        // .then(response => (
        //   console.log(response.data),
        //   this.items = response.data
        //   ))
        // .catch(error => (
        //   console.log(error.response),
        //   this.response = error.response
        //   ))
        item
      }
    },
    cancelClick: function(){
      this.activeEdit = false;
    }
  },
  beforeMount(){
    if(!this.$session.exists() || this.$session.get('tokken') == "") this.$router.push('/log')
    axios.get(
    'http://127.0.0.1:5000/items',
    { headers: {'Authorization': "Bearer "+this.$session.get('tokken')}}
    )
    .then(response => (
      console.log(response.data),
      this.items = response.data
      ))
    .catch(error => (
      console.log(error.response),
      this.response = error.response
      ))
    
  },
}
</script>
 
<style >
  .list-left-panel{
    display: flex;
    flex-direction:column;
    align-items: center;
    width:35%;
    height: 84vh;
    background: #663EFF;
    float:left;
  }
  .list-right-panel{
    display: flex;
    flex-direction:column;
    align-items: center;
    position: relative;
    left: 35%;
    margin: 0;
    padding: 4% 2%;
    background: #18ADD6; 
    width:61%; 
  }
  .list-left-panel-edit-item{

  }
</style>
