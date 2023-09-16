

<template>
<h1 class="text-white ">
  penis
</h1>
</template>

<style scoped>

</style>

<script setup>
import {onMounted} from 'vue'
import axios from 'axios'
import {useRoute} from 'vue-router'

onMounted(() =>{
  getProfile()
})

const route = useRoute()
function getProfile(){
  console.log('getting profile')

  axios
      .get(`/query/profile/${route.params.name}/`)
      .then(response=>{
        console.log('response:', response.data)
      })
      .catch(error =>{
        console.log('error', error)
      })
}

</script>