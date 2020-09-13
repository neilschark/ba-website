<template>
  <div class="home">
    <ButtonPage msg="Welcome to the demo frontend"/>
  </div>
</template>

<script>
// @ is an alias to /src
import ButtonPage from '@/components/ButtonPage.vue';

export default {
  name: 'Home',
  components: {
    ButtonPage,
  },
};
</script>
