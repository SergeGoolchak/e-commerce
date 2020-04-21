<script>

	import { onMount, onDestroy } from 'svelte';
    import Cookies from 'js-cookie/src/js.cookie.js'

   let wear = [];

    function getRef(id) {return document.getElementById(id).href;};

    const CSRF_TOKEN = Cookies.get('csrftoken');
    const PRODUCT_URL = getRef("product-ref");

    onMount(async () => { const response = await fetch(PRODUCT_URL, {
                            headers: {
                                'Accept': 'application/json, text-plain, */*',
                                'X-Requested-With': 'XMLHttpRequest',
                            }, });
        let wear_json = await response.json();
        wear = wear_json['product'];
        wear = wear;
        console.log(wear);
        console.log(typeof(wear));
    });

</script>

<main>

	<section class="related-product spad">
		<div class="container">
			<div class="row">
				<div class="col-lg-12 text-center">
					<div class="section-title">
						<h2>Related Products</h2>
					</div>
				</div>
			</div>
			<div class="row">
			{#each wear as item }
				<div class="col-lg-3 col-sm-6">
					<div class="single-product-item">
						<figure>
							<a href="."><img src='/static/shop/img/{item.img}' alt=""></a>
							<div class={item.status}>{item.status_text}</div>
						</figure>
						<div class="product-text">
							<h6>{item.name}</h6>
							<p>{item.price}</p>
						</div>
					</div>
				</div>
				{/each}
			</div>
		</div>
	</section>


</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>