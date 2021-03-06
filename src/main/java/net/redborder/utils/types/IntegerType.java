package net.redborder.utils.types;

import java.util.Map;
import java.util.Random;

public class IntegerType implements Type {
    private Random randomGen = new Random();
    private Integer max, min;
    private Boolean negative;

    public IntegerType(Map<String, Object> params) {
        this.max = (Integer) params.get("max");
        this.min = (Integer) params.get("min");
        this.negative = (Boolean) params.get("negative");
        if (this.max == null) this.max = Integer.MAX_VALUE;
        if (this.min == null) this.min = 0;
    }

    @Override
    public Object get() {
        Integer rand = (randomGen.nextInt(max - min) + min);
        if (negative != null && negative) { rand *= -1; }
        return rand;
    }
}
