<template>
    <notification v-if="errors && errors.length > 0" :type="type" :message="errors" @hide="clearErrors" />
    <form name="movieForm" id="movieForm" @submit.prevent="saveMovie">
        <div class="form-group mb-3">
            <label for="title" class="form-label">Movie Title</label>
            <input type="text" name="title" class="form-control" />
        </div>
        <div class="form-group mb-3">
            <label for="description" class="form-label">Movie Description</label>
            <textarea rows="5" cols="33" name="description" class="form-control" />
        </div>
        <div class="form-group mb-3">
            <label for="poster" class="form-label">Movie Poster</label>
            <input type="file" name="poster" class="form-control" />
        </div>
        <div class="form-group mb-3">
            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
    </form>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";
import  notification  from "@/components/Notifications.vue";

let csrf_token = ref("");
let errors = ref([]);
let type = "danger";

onMounted(() => {
    getCsrfToken();
});

function getCsrfToken() {
    fetch("http://localhost:8080/api/v1/csrf-token")
        .then((response) => response.json())
        .then((data) => {
            csrf_token.value = data.csrf_token;
        })
        .catch(function (error) {
            console.log(error);
        });
}

function clearErrors() {
      errors.value = [];
    }

function saveMovie() {
    let movieForm = document.getElementById("movieForm");
    let form_data = new FormData(movieForm);
    fetch("http://localhost:8080/api/v1/movies", {
        method: "POST",
        body: form_data,
        headers: {
            "X-CSRFToken": csrf_token.value,
        },
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            if (data.errors && data.errors.length > 0) {
                console.log(data.errors);
                errors.value = data.errors;
            } else {
                // display a success message
                console.log("Success");
                console.log(data);
                window.location.href = "/movies/view";
            }
        })
        .catch(function (error) {
            console.log(error);
        });
}
</script>
<style>
/* Add any component specific styles here */
</style>
