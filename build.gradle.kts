plugins {
    kotlin("multiplatform") version "1.3.72"
}

repositories {
    mavenCentral()
}

kotlin {
    macosX64("native") {
        binaries {
            executable{
                entryPoint = "ru.tano.tools.gpc.main"
            }
        }
    }
}

tasks.withType<Wrapper> {
    gradleVersion = "6.4.1"
    distributionType = Wrapper.DistributionType.ALL
}
