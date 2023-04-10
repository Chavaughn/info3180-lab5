<script>
import { ref } from "vue";
import  Movies  from "@/components/Movies.vue";
export default {
    name: "MoviesView",
    components:{
        Movies,
    }
};
</script>

<template >
    <div class="container">
        <Movies />
    </div>
</template>

<style>

</style>