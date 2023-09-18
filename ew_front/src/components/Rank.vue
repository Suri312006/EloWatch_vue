<script>
export default {
  name: "Rank",
  props: {
    rank_data: Object,
    required: true,
  }
}
</script>

<template>

  <link href="https://fonts.googleapis.com/css2?family=Nova+Mono&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Nova+Mono&family=PT+Mono&display=swap" rel="stylesheet">

 <div class="bg-black  border-amber-50 border-8">
  <img class="rounded col-span 2" :src="rank_data.icon_path" :alt="rank_data.tier">

   <div>

    <h1 class="text-blue-700">
      {{ rank_data.tier}}
    </h1>

  </div>
</div>
</template>

<style scoped>
/* Add any additional styling you want for your search bar here */
/* Add any additional styling you want for your toolbar here */
.font-nova-mono {
  font-family: 'Nova Mono', monospace;
  /* You can adjust the font size, letter spacing, and other properties here */
  letter-spacing: 0px;

}
.text-glow{
  text-shadow: 2px 2px 3px rgba(255, 255, 255, 0.5);
}
.font-nova-pt-mono{

font-family: 'PT Mono', monospace;

}
</style>