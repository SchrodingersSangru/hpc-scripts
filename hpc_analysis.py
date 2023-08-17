import numpy as np
import multiprocessing

# Simulate particle dynamics
def simulate_particle_dynamics(particles, num_steps):
    for _ in range(num_steps):
        particles += np.random.normal(0, 0.1, particles.shape)

# Calculate statistics for a subset of particles
def calculate_statistics(particles_subset):
    mean = np.mean(particles_subset)
    std_dev = np.std(particles_subset)
    return mean, std_dev

def main():
    num_particles = 10000
    num_steps = 1000
    num_processes = multiprocessing.cpu_count()

    particles = np.zeros(num_particles)
    simulate_particle_dynamics(particles, num_steps)

    chunks = np.array_split(particles, num_processes)
    
    pool = multiprocessing.Pool(processes=num_processes)
    results = pool.map(calculate_statistics, chunks)
    pool.close()
    pool.join()

    mean_results = [result[0] for result in results]
    std_dev_results = [result[1] for result in results]

    overall_mean = np.mean(mean_results)
    overall_std_dev = np.sqrt(np.sum(np.square(std_dev_results))) / num_processes
    
    print("===== HPC Data Analysis =====")
    print("Overall Mean:", overall_mean)
    print("Overall Standard Deviation:", overall_std_dev)

if __name__ == "__main__":
    main()
