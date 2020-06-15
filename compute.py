
def input():

def configure():
	#take strain tensors and decompose into principal strains (strain_tensor_toolbox eigenvectors)
	#first principal strain has direction, magnitude
	#second principal strain has sign (+/-)
	#turn into points in 3D (x, y, z)

def cluster():

	def group_by_first(pairs):
    	keys = []
    	for key, _ in pairs:
        	if key not in keys:
            	keys.append(key)
    	return [[y for x, y in pairs if x == key] for key in keys]

	def group_by_centroid(restaurants, centroids):
    #Return a list of clusters, where each cluster contains all eigs nearest to a corresponding centroid in centroids. 
    	d = []
    	for eig in eigs:
        	cent = find_closest(converted_eig(eig), centroids)
        	d.append([cent, eig])
    	return group_by_first(d)
    # END Question 4


def find_centroid(cluster):
    x = mean([converted_eig(i)[0] for i in cluster])
    y = mean([converted_eig(i)[1] for i in cluster])
    z = mean([converted_eig(i)[2] for i in cluster])
    return [x, y, z]

	def k_means(eigenvectors, k, max_updates = 200):
		assert len(eigenvectors) >= k,
		prev_centroids, n = [], 0
		centroids = [converted_eig(r) for r in sample(eigenvectors, k)]

		while prev_centroids != centroids and n < max_updates:
        	prev_centroids = centroids
            clusters = group_by_centroid(restaurants, prev_centroids)
        	centroids = [find_centroid(i) for i in clusters]
        	n += 1
        return centroids


def output():