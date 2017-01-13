import com.typesafe.sbt.packager.MappingsHelper._

name := "ambari-presto-service"

version := "0.161"

scalaVersion := "2.12.1"

val metaInfoConfig: String = "presto/metainfo.xml"

lazy val `ambari-presto-service` = project
  .in(file("presto"))
  .enablePlugins(UniversalPlugin)
  .settings(
    version := "0.161",
    topLevelDirectory := Some("PRESTO"),
    mappings in(Universal, packageBin) ++= {
      println(contentOf("presto").map(_._1.getPath))
      contentOf("presto")
        .filter(v => v._2 != "metainfo.xml")
        .filter(v => v._2 != "docs")
        .filter(v => v._2 != "tests")
        .filter(v => !v._1.getPath.startsWith("presto/target"))
    },
    mappings in(Universal, packageBin) += {
      val buildVersion = version.value + "-build-" + sys.env.getOrElse("BUILD_NUMBER", "local")
      val content =
        IO.read(file(metaInfoConfig)).replaceAll("<version>.*</version>", s"<version>$buildVersion</version>")
      val templateFile = file(target.value.getAbsolutePath + "/" + metaInfoConfig)
      IO.write(templateFile, content)
      templateFile
    } -> "metainfo.xml"
  )