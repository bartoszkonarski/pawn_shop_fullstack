<template>
  <section>

      <div class="list-left-panel">
        <EditTiles v-if="activeId"/>
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
        v-on:edit="changeEdit(item.id)"
        />
        <br>
      </div>

  </section>
</template>

<script>
import tiles from './listItem/tiles.vue'
import editTiles from './listItem/editTiles.vue' //VS Code ocipiał

export default {
  name: 'listItem',
  components: {
    Tiles: tiles,
    EditTiles: editTiles,
  },
  data: () => {
    return{
      items: [
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 1},
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 2},
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 3},
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 4},
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 5},
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 6},
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 7},
      ],
      activeId: 0,
      activeItem: {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 7}
    }
  },
  methods: {
    changeEdit: function(prop) {
      this.activeId = prop
    }
  },
  watch: {
    activeId: function(){

    },
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
