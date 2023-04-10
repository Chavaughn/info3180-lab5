<template>
    <div>
      <h1>Movies</h1>
      <hr>
      <div class="movies">
        <div class="card-container" v-for="movie in movies" :key="movie.id">
          <div class="card">
            <img :src="movie.poster" alt="Movie Poster" />
            <div class="card-body-out">
              <div class="card-body">
                <div class="title-box">
                  <h5 class="card-title">{{ movie.title }}</h5>
                </div>
                <div class="description-box">
                  <p class="card-text">{{ movie.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  import { RouterLink } from "vue-router";
  
  let movies = ref([]);
  
  async function fetchMovies() {
    try {
      const response = await fetch("http://localhost:8080/api/v1/movies");
      const data = await response.json();
      movies.value = data.movies;
    } catch (error) {
      console.log(error);
    }
  }
  
  onMounted(() => {
    fetchMovies();
  });
  
  </script>
  
  <style>
  .movies {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    row-gap: 3vh;
    padding: 2vh;
  }
  
  .card-container {
    margin-bottom: 2vh;
  }
  
  .card {
    display: flex;
    flex-direction: row;
    max-width: 400px;
    max-height: 400px;
    height: 35vh;
    width: 80vw;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    overflow: hidden;
  }
  
  img {
    max-width: 44%;
    max-height: 100%;
    object-fit: cover;
  }
  
  .card-body-out {
    padding: 1rem;
    padding-top: 0;
    overflow: hidden;
  }
  
  .card-body {
    overflow: scroll;
    max-height: 100%;
    display: flex;
    flex-direction: column;
  }
  
  .title-box {
    position: sticky;
    top: 0;
    background-color: white;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    border-bottom: 1px solid rgba(0, 0, 0, 0.2);
  }
  
  .card-title {
    margin-bottom: 0;
  }
  
  .description-box {
    margin-bottom: 0.5rem;
  }
  
  .card-text {
    margin-bottom: 0;
  }
  
  .card-body::-webkit-scrollbar {
    width: 0.5em;
  }
  
  .card-body::-webkit-scrollbar-track {
    background-color: #f5f5f500;
  }
  
  .card-body::-webkit-scrollbar-thumb {
    background-color: #00000000;
  }
  
  </style>
  