<script>
import { ref } from "vue";
import  MovieForm  from "@/components/MovieForm.vue";
export default {
    name: "AddMovieFormView",
    components:{
        MovieForm,
    }
};
</script>

<template >
    <div class="container">
        <MovieForm />
    </div>
</template>

<style>
.container{
    align-items: flex-start;
    display: flex;
    flex-direction: column;
    width: 100%;
}
</style>