from cancer_gene_data import read_data
import sklearn

def calc_w(data,kmeans_fit):
    centorids = [kmeans_fit.cluster_centers_[label] for label in kmeans_fit.labels]
    import pdb; pdb.set_trace()  # breakpoint 31cb6e99 //
    return False

def run_kmeans():
    gene_names, data = read_data()

    kmean_fit = sklearn.cluster.KMeans(1)

    kmean_fit.fit(data)

if __name__ == '__main__':
    run_kmeans()
