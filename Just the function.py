def proc_gen():
    # generating the map
    global map_list
    map_list = []
    noise = PerlinNoise(octaves = 1.5, seed = seed)
    block_size = 10  # Increase block size to reduce iterations
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            n = noise([x / width, y / height])
            g = int((n + 1) / 2 * 255)  # Scale noise value to 0-255
            if n < 0:
                g = GREEN
            elif n < 0.0042:
                g = YELLOW
            if g == GREEN:
                pygame.draw.rect(screen, g, (x, y, block_size, block_size))
            pygame.draw.rect(screen, g , (x, y, block_size, block_size))
            num = round(n, 5)
            map_list.append(num)
