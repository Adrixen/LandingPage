			function addImageLink(src) {
				var gallery = document.getElementById('gallery2');
				var newLink = document.createElement('a');
				newLink.style.display = 'none';
				newLink.href = src;
				var newImage = document.createElement('img');
				newImage.src = src;
				newLink.appendChild(newImage);
				gallery.appendChild(newLink);
			}

			// Add new image links automatically
			var newImageSrcs = [
				'galerie/galeria2/2.jpg',
				'galerie/galeria2/3.jpg',
				'galerie/galeria2/4.jpg',
				// Add more image sources here
			];

			for (var i = 0; i < newImageSrcs.length; i++) {
				addImageLink(newImageSrcs[i]);
			}