<script>
    import { onMount } from 'svelte';
    let projects = [];

    onMount(async () => {
        const res = await fetch('http://localhost:8000/api/projects/');
        projects = await res.json();
    });
</script>

<style>
    /* Add your styles here */
</style>

<main>
    <h1>Failed Projects</h1>
    <ul>
        {#each projects as project}
            <li>{project.title}: {project.description}</li>
        {/each}
    </ul>
</main>