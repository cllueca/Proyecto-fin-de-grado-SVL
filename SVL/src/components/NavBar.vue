<template>
    <nav class="navbar bg-light">
        <div class="container" id="navbar">
            <router-link to="/" class="navbar-brand">
            <img src="../components/icons/logoSVL.png" alt="Bootstrap" width="100" height="100">
            </router-link>
        </div>
    </nav>
</template>

<style>
    #navbar{
        display: flex;
        justify-content: center;
    }

    @media (max-width: 400px) {
        #navbar img{
            margin-top:-10px;
            height: 50px;
            width: 50px;
        }

        #navbar{
            height: 40px;
        }
    }
</style>