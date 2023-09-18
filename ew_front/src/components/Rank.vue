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
<!--<img-->
<!--        :src="rank_data.icon_path"-->
<!--        alt="penis"-->
<!--        class="rounded col-span 2"-->
<!--    >-->
<div v-if="rank_data.icon_path">
  <h1 class="text-blue-700">
    {{ rank_data.icon_path}}
  </h1>
</div>
</template>

<style scoped>

</style>