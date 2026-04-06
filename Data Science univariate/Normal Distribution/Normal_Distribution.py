import pandas as pd
import seaborn as sns
class Normal_distribution:
    def get_pdf_probability(dataset,startrange,endrange):
        from matplotlib import pyplot 
        from scipy.stats import norm
        ax=sns.distplot(dataset,kde=True,kde_kws={'color':'gold'},color='blue')
        pyplot.axvline(startrange,color='green')
        pyplot.axvline(endrange,color='red')
       
        sample=dataset
        sample_mean=sample.mean()
        sample_std=sample.std()
        print('Mean=%.3f, Standard Deviation=%.3f' % (sample_mean, sample_std))
        pyplot.show()
        dist=norm(sample_mean,sample_std)
        values=[value for value in range(startrange,endrange)]
        probabilities=[dist.pdf(value)for value in values]
        prob=sum(probabilities)
        print("The area between range({},{}):{}".format(startrange,endrange,sum(probabilities)))
        return prob